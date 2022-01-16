
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
from ipywidgets import Widget
import fileupload
import io
import sys


global file_contents
def uploader():
    
    uploader_widget = fileupload.FileUploadWidget()

def ucb(change):
    
    decoded = io.StringIO(change['owner'].data.decode('utf-8'))
    filename = change['owner'].filename
    print('Uploaded `{}` ({:.2f} kB)'.format(
        filename, len(decoded.read()) / 2 **10))
    file_contents = decoded.getvalue()

    _upload_widget.observe(ucb, names='data')
    display(_upload_widget)

    _upload()

def Calculate_Frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = ['''!()-[]{};:'"\,<>./?@#$%^&*_~''']
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]


    New_contents=file_contents.split(",")
    new_dict={}
    for word in New_contents:
        if word.isalpha()==True and word not in uninteresting_words:

            word=word.lower()
            new_dict[word]=New_contents.count(word)


    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(new_dict)
    return cloud.to_array()

myimage = Calculate_Frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()
