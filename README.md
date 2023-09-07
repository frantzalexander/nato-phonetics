# NATO-Phonetics


## Project Overview
This is a tool to improve the communication for the spelling of words and names.

## Objectives
- Prompt user for input
- Take user input and separate each letter.
- Associate each letter with a NATO Phonetic word.
- Display each phonetic word in a list to the user.

## Results
![image](https://github.com/frantzalexander/nato-phonetics/assets/128331579/b88ebe1a-f06a-4d9d-8f2f-94a00594fdac)

## Process

```mermaid
flowchart TD
start(((START)))
import[Import NATO Phonetic Dataset]
create_dict[Associate Each Letter with Phonetic Word]
input[Prompt for User Input]
error_handling{Screen for User Errors}
output[Output Phonetic Word List]
finish(((END)))
start --> import
import --> create_dict
create_dict --> input
input --> error_handling
error_handling -->|No Input Errors|output
error_handling -->|User Input Error|input 
output --> finish
