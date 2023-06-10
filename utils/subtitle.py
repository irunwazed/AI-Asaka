

def generate_subtitle(name_file, _text):
    # output.txt will be used to display the subtitle on OBS
    with open(name_file, "w", encoding="utf-8") as outfile:
        try:
            text = _text
            words = text.split()
            lines = [words[i:i+10] for i in range(0, len(words), 10)]
            for line in lines:
                outfile.write(" ".join(line) + "\n")
        except:
            print("Error writing to output.txt")

