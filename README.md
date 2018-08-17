# Language-Detector

Detect the programming language that given text files are written in (considering C++, Python and Java).

Python version: 3.7.0

INSTRUCTIONS

	Put the files that you want to test correctly separated in 'cpp', 'java' and 'python' directories.
	Run the script to see a summary of the prediction results. 

FUNCTIONS

	add_keywords(python_kw, cpp_kw, java_kw)
		Fill lists python_kw, cpp_kw and java_kw with python, cpp and java keywords.
		
	word_frequency(file)
		Return a Counter structure with the number of appearances of each word in the given file.
		
	guess_language(file)
		Return the predicted language - considering cpp, python and java - for the given file.
		
	main()
		Test guess_language with all files placed in 'cpp/', 'python/' and 'java/' directories, printing a summary of the results.
