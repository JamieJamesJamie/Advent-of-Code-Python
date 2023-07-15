// <copyright file="DirectoryInfoExtensions.cs" company="JamieJamesJamie">
// Copyright (c) JamieJamesJamie. All rights reserved.
// </copyright>

using System.IO;
using System.Runtime.CompilerServices;

namespace Advent.Of.Code.Helpers.Extensions
{
    public static class DirectoryInfoExtensions
    {
        public static DirectoryInfo RequiredParent(this DirectoryInfo directoryInfo)
        {
            var parent = directoryInfo.Parent;

            ArgumentNullException.ThrowIfNull(parent);

            return parent;
        }
    }
}
