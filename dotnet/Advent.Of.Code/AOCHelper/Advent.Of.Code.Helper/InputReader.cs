// <copyright file="InputReader.cs" company="JamieJamesJamie">
// Copyright (c) JamieJamesJamie. All rights reserved.
// </copyright>

namespace Advent.Of.Code.Helper;

using FileParser;

public class InputReader<T>
{
    private readonly string inputFilePath;

    public InputReader(string inputFilePath) => this.inputFilePath = inputFilePath;

    public IEnumerable<T> ReadInputAsLines()
    {
        IParsedFile file = new ParsedFile(this.inputFilePath);


        while (!file.Empty)
        {
           
        }


        StreamReader reader = new(this.inputFilePath);
        string line;

        while ((line = reader.ReadLine()) != null)
        {
            yield return ParseL
        }
    }
}
