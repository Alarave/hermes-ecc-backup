param(
    [string]$Keyword = ""
)

$Paths = @(
    "$env:USERPROFILE\.gemini\antigravity\skills",
    "E:\skill claude\skill claude"
)

$Results = @()

foreach ($Path in $Paths) {
    if (Test-Path $Path) {
        $SkillFiles = Get-ChildItem -Path $Path -Recurse -Filter "SKILL.md" -File -ErrorAction SilentlyContinue
        foreach ($File in $SkillFiles) {
            $Content = Get-Content $File.FullName -Raw
            
            # Simple regex to extract name and description from YAML frontmatter
            $Name = ""
            $Description = ""
            
            if ($Content -match 'name:\s*(.+)') {
                $Name = $matches[1].Trim()
            }
            if ($Content -match 'description:\s*(.+)') {
                $Description = $matches[1].Trim()
            }
            
            if ($Name -ne "") {
                $Results += [PSCustomObject]@{
                    Name = $Name
                    Description = $Description
                    Path = $File.DirectoryName
                }
            }
        }
    }
}

if ($Keyword -ne "") {
    $Results = $Results | Where-Object { $_.Name -match $Keyword -or $_.Description -match $Keyword }
}

$Results | Format-Table -Property Name, Description -AutoSize -Wrap
