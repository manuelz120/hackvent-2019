const CellularAutomata = require("cellular-automata");
const { flatten, cloneDeep } = require("lodash");
const Jimp = require("jimp");
const QrDecoder = require("node-zxing");

async function createImage(filename, data, size) {
  const image = await Jimp.create(size, size);

  for (let y = 0; y < size; y++) {
    for (let x = 0; x < size; x++) {
      const item = data[y * size + x];
      image.setPixelColor(!item ? 0xffffffff : 0xff000000, x, y);
    }
  }

  await image.writeAsync(filename);
}

async function createQrCode(filename, data, size) {
  createImage(filename, data, size);
  const qrDecoder = new QrDecoder();

  return await new Promise(resolve =>
    qrDecoder.decode(filename, (error, code) => resolve([error, code]))
  );
}

function performEvolutionWithRule(data, rule, size, iterations = 1) {
  const cellularAutomata = new CellularAutomata([size]);
  cellularAutomata.setRule(`W${rule}`);
  cellularAutomata.array.data = flatten(data);

  cellularAutomata.iterate(iterations);

  return Array.from(cellularAutomata.array.data);
}

async function readImageData(filename) {
  const inputImage = await Jimp.read(filename);
  const width = inputImage.getWidth();
  const height = inputImage.getHeight();
  const data = [];
  for (let y = 0; y < height; y++) {
    for (let x = 0; x < width; x++) {
      const color = inputImage.getPixelColor(x, y);
      data.push(color > 255 ? 0 : 1);
    }
  }
  return { width, height, data };
}

function createXorMask(width, height) {
  let row = new Array(width * 2 + 1);
  row.fill(0);
  row[width] = 1;
  const rows = [];
  rows.push(row);

  while (rows.length < height) {
    const transformedRow = performEvolutionWithRule(row, 30, row.length);
    rows.push(transformedRow);
    row = cloneDeep(transformedRow);
  }

  return rows;
}

(async function() {
  const { width, height, data } = await readImageData("./input.png");

  const maskData = createXorMask(width, height);

  let foundFlag = false;
  let startIndex = 0;

  while (!foundFlag && startIndex < maskData[0].length) {
    const flagData = cloneDeep(data);

    for (let y = 0; y < 33; y++) {
      for (let x = 0; x < 33; x++) {
        flagData[y * 33 + x] ^= maskData[y][startIndex + x];
      }
    }
    const filename = `./flag.jpg`;
    const [_, code] = await createQrCode(filename, flagData, 33);
    foundFlag = code.length > 0;

    if (foundFlag) {
      console.log(`Got flag: ${code}`);
    }

    startIndex++;
  }
})();
