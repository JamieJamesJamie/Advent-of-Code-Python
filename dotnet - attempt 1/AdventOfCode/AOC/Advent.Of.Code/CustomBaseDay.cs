// <copyright file="CustomBaseDay.cs" company="JamieJamesJamie">
// Copyright (c) JamieJamesJamie. All rights reserved.
// </copyright>

using Advent.Of.Code.Helpers;
using Advent.Of.Code.Helpers.Extensions;

namespace Advent.Of.Code;

/// <summary>
/// <see cref="BaseDay"/> enforcing a preliminary parsing of input data.
/// </summary>
public abstract class CustomBaseDay : BaseDay
{
#pragma warning disable S1699 // Constructors should only call non-overridable methods
    /// <summary>
    /// Initializes a new instance of the <see cref="CustomBaseDay"/> class.
    /// </summary>
    protected CustomBaseDay() => this.ParseInput();
#pragma warning restore S1699 // Constructors should only call non-overridable methods

    /// <summary>
    /// Parses input.
    /// </summary>
    protected abstract void ParseInput();

    protected override string InputFileDirPath
    {
        get
        {
            return Path.Combine(
                VisualStudioProvider
                    .GetRequiredSolutionDirectoryInfo()
                    .RequiredParent()
                    .RequiredParent()
                    .RequiredParent()
                    .RequiredParent()
                    .FullName,
                "puzzle_inputs"
            );
        }
    }

    public virtual uint CalculateYear()
    {
        var typeName = GetType().Name;
        var
    }
}
