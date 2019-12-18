using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HV1918
{
    class Program
    {
        static void Main(string[] args)
        {
            var encrypted = StringToByteArray("096CD446EBC8E04D2FDE299BE44F322863F7A37C18763554EEE4C99C3FAD15");
            var salsa = new Salsa20();
            var iv = "11458fe7a8d032b1";
            var decryptor = salsa.CreateDecryptor(StringToByteArray("0320634661b63cafaa76c27eea00b59bfb2f7097214fd04cb257ac2904efee46"),
                StringToByteArray(iv));
            var output = new byte[encrypted.Length];
            decryptor.TransformBlock(encrypted, 0, encrypted.Length, output, 0);

            Console.WriteLine(Encoding.ASCII.GetString(output));

            Console.ReadLine();
        }

        public static byte[] StringToByteArray(string hex)
        {
            return Enumerable.Range(0, hex.Length)
                             .Where(x => x % 2 == 0)
                             .Select(x => Convert.ToByte(new string(hex.Substring(x, 2).ToArray()), 16))
                             .ToArray();
        }
    }
}
