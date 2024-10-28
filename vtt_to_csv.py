import webvtt
import pandas as pd

file_name_in = input("Enter the path to a .vtt file: ")
vtt_file = webvtt.read(file_name_in)
df = pd.DataFrame(columns=['Start Time', 'End Time', 'Speaker', 'Text'])

i = 0
for caption in vtt_file:
    start = caption.start
    end = caption.end
    df.loc[i] = [start] + [end] + caption.text.split(": ")
    i += 1

#the transcript in csv format will be saved in the same directory that the vtt file came from
file_name_out = file_name_in.replace('.vtt', '.csv')
df.to_csv(file_name_out, encoding='utf-8', index=False)