import csv
import openai

updated_csv = []
final_csv = []
first_row = []
with open('sample_csv.csv', 'r') as csv_file:
#     first_row.append(next(csv_file))
#     print(csv_file)
    reader = csv.reader(csv_file)
    reader = list(reader)
    for i in range(len(reader[0])):
        first_row.append(reader[0][i])
    for row in reader[1:]:
        updated_csv.append(row)

openai.api_key = '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'

def generate_chat_response(question):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=question,
        max_tokens=50
    )
    chat_gpt_response = response.choices[0].text.strip()
    return chat_gpt_response

final_csv.insert(0,first_row)
for row in updated_csv:
    question = f'{row[0]} developer with experience in {row[1]} earnes how much'
    response = generate_chat_response(question)
    row[2] = response
    final_csv.append(row)

with open('sample_csv.csv', 'w', newline='') as writing_csv:
    csvwriter = csv.writer(writing_csv)
    csvwriter.writerows(final_csv)