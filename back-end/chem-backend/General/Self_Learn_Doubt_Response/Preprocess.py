import string
import bs4 as bs
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer


class Preprocess(object):

    def remove_html_tags(self, data_frame):
        for index, row in data_frame.iterrows():
            soup = bs.BeautifulSoup(row['html_text'], 'html.parser')
            data_frame.loc[index, "no_html_text"] = soup.get_text()
        print('html tags')
        return data_frame

    def line_space_removal(self, data_frame):
        for index, row in data_frame.iterrows():
            lines = row['no_html_text'].split("\n")

            not_empty_lines = [line for line in lines if line.strip() != ""]

            processed_lines = ""
            for line in not_empty_lines:
                processed_lines += line + "\n"
                data_frame.loc[index, "text"] = processed_lines
        print('line space')
        return data_frame

    def sentence_punctuation(self, data_frame):
        exclude = set(string.punctuation)
        all_docs_list = []

        for index, rows in data_frame.iterrows():
            text = rows['text']
            text = ''.join(ch for ch in text if ch not in exclude)
            all_docs_list.append(text)
        print('punctuation')
        return all_docs_list

    def word_tokenizer(self, texts):
        plot_data = [[]] * len(texts)

        for text in texts:
            token_text = word_tokenize(text)
            plot_data[len(texts) - 1].append(token_text)
        print('tokenizer')
        return plot_data

    def lowercase(self, data_frame, plot_data):
        for x in range(len(data_frame.name)):
            lowers = [word.lower() for word in plot_data[0][x]]
            plot_data[0][x] = lowers
        print('lowercase')
        return plot_data

    def stopwords(self, data_frame, plot_data):

        stop_words = set(stopwords.words('english'))

        for x in range(len(data_frame.name)):
            filtered_sentence = [w for w in plot_data[0][x] if not w in stop_words]
            plot_data[0][x] = filtered_sentence
        print('stopwords')
        return plot_data

    # def stemming(self, data_frame, sentences):
    #     snowball_stemmer = SnowballStemmer("english")
    #     for x in range(len(data_frame.name)):
    #         stemmed_sentence = [snowball_stemmer.stem(w) for w in sentences[0][x]]
    #     print('stemming')
    #     return stemmed_sentence

    def preprocess_text(self, data_frame):
        html_tagless = self.remove_html_tags(data_frame)
        line_removal = self.line_space_removal(html_tagless)
        punctuation_removal = self.sentence_punctuation(line_removal)
        tokenize = self.word_tokenizer(punctuation_removal)
        convert_lowercase = self.lowercase(data_frame, tokenize)
        stop_words = self.stopwords(data_frame, convert_lowercase)
        # stem_words = self.stemming(data_frame, stop_words)
        print(convert_lowercase)
        return convert_lowercase
