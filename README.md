# Preservica Ingest Folder Structure

This is a script to organise files into Preservica's multiple manifestation folder structure prior to ingest

This is for files are that already labelled with correct references numbers and require a folder with the same name

This script requires all files and formats to be loose in the same folder and to have matching names across formars

This script mirrors Preservicas multiple manifestation hierarchy for Preservation and Access copies

For example; if only one format is present, the file gets moved into sub-folder named after itself, if multiple formats are presents, then further sub-folders are made as so;

2 Preservation copies:
- Preservica_preservation1_lnk
- Preservica_preservation2_lnk

1 Preservation and 1 access copy
- Preservica_preservation1_lnk
- Preservica_presentation2_lnk

2 Preservation and 1 access copy
- Preservica_preservation1_lnk
- Preservica_preservation2_lnk
- Preservica_presentation3_lnk
