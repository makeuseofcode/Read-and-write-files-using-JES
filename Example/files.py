
def readFromFile():
  file = pickAFile() # Asks user to select a file to read from
  
  if not file.endswith(".txt") and not file.endswith(".csv"):
    print("Error: Only .txt and .csv files are supported.")
    return
    
  openedFile = open(file, "rt") # Opens file. "rt" means we will open the file for reading purposes.
  
  allContent = openedFile.read() # read() stores all content from the file into a string
    
  openedFile.close() # Close file after reading its contents
  
  # For lists
  if file.endswith(".txt"):
    rows = allContent.split("\n") # Since allContents is one string, this will separate the string based on the break line "\n". 
    print(rows)
  
  # For cells
  if file.endswith(".csv"): 
    rows = allContent.split("\n") # Split each row in the CSV file
    csvData = []
    for row in rows:
      if(row != ''):
        cells = row.split(",") # Split each cell and store it separately
        csvData.append([float(cell) for cell in cells]) # Append to the double array so it looks like this: [[1,2,3],[4,5,6],[7,8,9]].
    print(csvData)
  
  

def writeToFile():
  file = pickAFile() 
  
  openedFile = open(file, "at")  # Open the file for appending 
  #openedFile = open(file, "w")  # Open the file for writing
  
  if file.endswith(".txt"):
    openedFile.write("\nTesting") # - this line appends "testing" to the end of the file.
    openedFile.write("\nTesting1\nTesting2") # Will append multiple lines
    openedFile.write("\nTesting3")
  
  if file.endswith(".csv"): 
    openedFile.write("\n12,34,56") # - this line appends a new row with cell data to the end of the file.
    
  openedFile.close()
  print("Wrote to file successfully")
  
