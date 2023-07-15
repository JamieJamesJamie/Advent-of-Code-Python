// <copyright file="Program.cs" company="JamieJamesJamie">
// Copyright (c) JamieJamesJamie. All rights reserved.
// </copyright>

if (args.Length == 0)
{
    await Solver.SolveLast(options => options.ClearConsole = false);
}
else if (args.Length == 1 && args[0].Contains("all", StringComparison.CurrentCultureIgnoreCase))
{
    await Solver.SolveAll(options =>
    {
        options.ShowConstructorElapsedTime = true;
        options.ShowTotalElapsedTimePerDay = true;
    });
}
else
{
    IEnumerable<uint> indices = args.Select(
        args => uint.TryParse(args, out uint index) ? index : uint.MaxValue
    );
    await Solver.Solve(indices.Where(index => index < uint.MaxValue));
}
