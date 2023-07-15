// <copyright file="BaseSolver.cs" company="JamieJamesJamie">
// Copyright (c) JamieJamesJamie. All rights reserved.
// </copyright>

namespace Advent.Of.Code.Helper;

using AoCHelper;

/// <summary>
/// Abstract Base Class to solve Advent of Code puzzles.
/// </summary>
/// <typeparam name="TSolve">
/// The return type of the answers for both
/// part 1 and part 2 of the problem.
/// </typeparam>
public abstract class BaseSolver<TSolve> : BaseSolver<TSolve, TSolve> { }

/// <summary>
/// Abstract Base Class to solve Advent of Code puzzles.
/// </summary>
/// <typeparam name="TSolve1">The return type of the answer for part 1 of the problem.</typeparam>
/// <typeparam name="TSolve2">The return type of the answer for part 2 of the problem.</typeparam>
public abstract class BaseSolver<TSolve1, TSolve2> : BaseDay
{
    protected readonly string[] input;
    protected bool inputValid = false;

    /// <summary>
    /// Initializes a new instance of the <see cref="BaseSolver{TSolve1, TSolve2}"/> class.
    /// </summary>
    protected BaseSolver()
    {
        this.input = new string[1];

        if (File.Exists(InputFilePath))
        {
            this.input = File.ReadAllLines(this.InputFilePath);
            this.inputValid = true;
        }
        else
        {
            var task = AdventOfCodeService.FetchInput(CalculateYear(), CalculateIndex());
        }
    }

    /// <summary>
    /// Gets the problem's year.
    /// </summary>
    protected abstract uint Year { get; }

    /// <summary>
    /// Gets the prefix that each solver class should use.
    /// </summary>
    protected override string ClassPrefix => "Solver";

    /// <summary>
    /// Solves part 1 of the problem.
    /// </summary>
    /// <returns>
    /// A <see cref="ValueTask{string}"/> that represents
    /// the result of part 1 of the problem.
    /// </returns>
    public sealed override ValueTask<string> Solve_1() =>
        BaseSolver<TSolve1, TSolve2>.Solve(this.Solve1());

    /// <summary>
    /// Solves part 2 of the problem.
    /// </summary>
    /// <returns>
    /// A <see cref="ValueTask{string}"/> that represents
    /// the result of part 2 of the problem.
    /// </returns>
    public sealed override ValueTask<string> Solve_2() =>
        BaseSolver<TSolve1, TSolve2>.Solve(this.Solve2());

    /*protected InputReader<T> InputReader<T>(string? fileSuffix = null) =>
        new InputReader<T>(this.InputPath(fileSuffix));

    protected InputReader InputReader(string? fileSuffix = null) =>
        new InputReader(this.InputPath(fileSuffix));

    protected InputReader<T, U> InputReader<T, U>(string? fileSuffix = null) =>
        new InputReader<T, U>(this.InputPath(fileSuffix));*/

    /// <summary>
    /// Solves part 1 of the problem.
    /// </summary>
    /// <returns>The result of part 1 of the problem.</returns>
    protected abstract TSolve1 Solve1();

    /// <summary>
    /// Solves part 2 of the problem.
    /// </summary>
    /// <returns>The result of part 2 of the problem.</returns>
    protected abstract TSolve2 Solve2();

    private static ValueTask<string> Solve<TSolve>(TSolve? result)
    {
        ArgumentNullException.ThrowIfNull(result);
        string? resultString = result.ToString();
        ArgumentNullException.ThrowIfNull(resultString);

        return new(resultString);
    }

    /* private string InputPath(string? fileSuffix = null)
     {
         if (fileSuffix == null)
         {
             return this.InputFilePath;
         }
 
         string index = this.CalculateIndex().ToString("D2");
         return Path.Combine(
             this.InputFileDirPath,
             $"{index}.{fileSuffix}.{this.InputFileExtension.TrimStart('.')}"
         );
     }*/
}
