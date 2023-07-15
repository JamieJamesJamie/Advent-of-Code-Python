// <copyright file="VisualStudioProvider.cs" company="JamieJamesJamie">
// Copyright (c) JamieJamesJamie. All rights reserved.
// </copyright>

namespace Advent.Of.Code.Helpers
{
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using System.Text;
    using System.Threading.Tasks;

    public static class VisualStudioProvider
    {
        public static DirectoryInfo? TryGetSolutionDirectoryInfo(string? currentPath = null)
        {
            DirectoryInfo? directory = new(currentPath ?? Directory.GetCurrentDirectory());

            while (directory != null && !directory.GetFiles("*.sln").Any())
            {
                directory = directory.Parent;
            }

            return directory;
        }

        public static DirectoryInfo GetRequiredSolutionDirectoryInfo(string? currentPath = null)
        {
            DirectoryInfo? directoryInfo = VisualStudioProvider.TryGetSolutionDirectoryInfo(
                currentPath
            );
            ArgumentNullException.ThrowIfNull(directoryInfo);
            return directoryInfo;
        }
    }
}
