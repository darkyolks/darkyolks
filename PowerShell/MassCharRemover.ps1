# Define the folder path
$folderPath = "C:\Path\to\folder"

# Get all Markdown (.md) files in the folder, change extension if needed.
$files = Get-ChildItem -Path $folderPath -Filter *.md

# Loop through each file
foreach ($file in $files) {
    # Create the new filename by replacing ". . . . . . ." with an empty string
    $newFileName = $file.Name.Replace(". . . . . . .", "")

    # Rename the file only if the new name is different
    if ($newFileName -ne $file.Name) {
        Rename-Item -Path $file.FullName -NewName $newFileName
    }
}