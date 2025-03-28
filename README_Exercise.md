# Exercise Robot Capto

Welcome to the **Exercise Robot** project! This repository contains a very basic UI that allows you to upload files (PDF, DOCX, or otherwise). Your task is to implement the “business logic” behind this UI. In other words, you’ll need to handle the processing of uploaded documents, extraction of relevant data, and generation of a desired output file based on a single template.

## Exercise Summary

What you should achieve:

1. **Build a script that asks the user for an input file and returns a structured output**
2. **There are several input file examples that can be found in the "input" folder. Use these as a reference, but make sure that the UI works for any file of the same type**
3. **The required ouput file can be found in the "output" folder. This template needs to be completed with the data extracted from each input file**
4. **You should keep the structure as is in this repository**

Please pay attention to the details below as they will influence your success in this exercise.

## What Is This Exercise About?

The purpose of this exercise is to test how you:

1. **Read and parse a file (PDF in this instance).**
2. **Extract specific data (e.g., date-specific or region-specific data).**
3. **Transform and process data according to predefined rules or templates.**
4. **Generate a final output document in a consistent, structured format.**

We have intentionally provided only a bare-bones starter application. *There is no “backend logic” included.* You have full freedom to create the data extraction and reporting logic in whatever way you see fit.


## Process Blueprint

1. **Upload File Handling**
   - The starter project has a simple form or interface that accepts file uploads.
   - You are free to modify the upload mechanism or keep it as is.

2. **Business Logic Implementation**
   - Parse the uploaded file that can be selected by the user. It will be one of the files in the “input folder”. However, the UI should work with other files of the same type (Trade Registry).
   - Identify and extract the required data. For this exercise, the MUST EXTRACT information is highlighted in yellow in the output template (in “output folder”), whilst other fields that are NICE TO EXTRACT are highlighted in red. 
   - You may need libraries to handle PDF parsing or DOCX parsing, so be prepared to explore how best to parse each format.

3. **Template-Based Output**
   - We suggest using the **template** file for your final output document. This template might be a Word document, but it can be given to the user as PDF, whichever you prefer.
   - Inside the template, define placeholders or markers that represent the pieces of data you are extracting.
   - Implement logic that replaces those placeholders with actual data.
   - Keep the format of the template as is.

4. **Final Document Generation**
   - Once the data is placed into the correct fields in the template, generate a final file for the user to download or view.
   - You can choose to generate a PDF, or a new .docx file.

## Additional elements

1. **Input File**: PDF saved in "input" folder, containing registration information.
2. **Extraction Rules**: You only need to extract the information required to complete the highlighted values.
3. **Template**: The word document saved in the “output folder”.
4. **Output**: A finalized Word or PDF file, in the predefined format, that is completed with the correct data from the input file. Bonus: extracting the NICE TO EXTRACT values too.

## Getting Started

1. **Clone this repo**
   ```bash
   git clone https://github.com/Capto-Company/Exercise-Robot.git
   cd Exercise-Robot
   ```
   Install dependencies (if any are defined—otherwise, add your own as you work).
   Launch the app and confirm you can upload files via the UI.
   Implement your data parsing and file generation in the backend logic of your choice.

## Suggested Approach

- Research how to read the metadata and contents of PDF in the language/framework you’re using.
- Decide on a clear data structure or data model for storing extracted content.
- Design your template (e.g., a world file with placeholders).
- Code a way to replace placeholders with the actual data.
- Output the final generated document for download or viewing in the UI.

## Deliverables

- **Working Application**
  When you run the project and upload a file, the system should produce a final output ( PDF, DOCX—your choice) that reflects the extracted and processed data.

- **Documentation**
  A brief explanation (in code comments or in a separate doc) of how you approached the parsing and template generation.
  Include any assumptions made or limitations discovered.

## Evaluation
We will review your solution for:

- **Correctness**: Does it handle the file format correctly and extract the expected data?
- **Maintainability**: Is the code structured in a clean and logical way?
- **Reusability**: Could this logic be extended to handle more file types or templates?
- **Clarity**: Did you document (in code or in a separate file) how to run and test your solution?

## Contributing
If you have ideas or would like to improve the example, feel free to open a Pull Request or discuss changes via Issues.

## License
This exercise is provided as-is, for learning and testing purposes only. If you reuse or adapt it for your own projects, please link back to this repository and credit appropriately.

Happy coding! We look forward to seeing how you handle the exercise. If you have any questions, please don’t hesitate to ask.

#   p d f _ e x t r a c t o r _ t e s t  
 