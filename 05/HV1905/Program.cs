using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;

namespace HV1905
{
    class Program
    {
        static void Main(string[] args)
        {
            var colors = new List<Color>();
            var image = new Bitmap(@"./157de28f-2190-4c6d-a1dc-02ce9e385b5c.png");

            for (var y = 0; y < image.Height; y++)
            {
                for (var x = 0; x < image.Width; x++)
                {
                    var color = image.GetPixel(x, y);
                    if (!colors.Contains(color))
                    {
                        colors.Add(color);
                    }
                }
            }

            var lines = colors.Select(c => {
                return (char)c.B;
            }).ToArray();

            var flag = new string(lines).Substring(13, 35);

            Console.WriteLine(flag);

            Console.ReadLine();
        }

    }
}
