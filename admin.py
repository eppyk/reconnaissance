def write_to_file(directory, filename, result):
    file = open(directory+"/"+filename , "w")
    file.write(result)
    file.close()
