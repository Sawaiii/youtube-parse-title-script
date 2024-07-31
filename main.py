from pytube import YouTube

def get_video_title(url):
    try:
        yt = YouTube(url)
        title = yt.title
        return f"{url} - {title}"
    except Exception as e:
        return f"{url} - Произошла ошибка: {e}"

def process_links(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            links = infile.readlines()

        with open(output_file, 'w') as outfile:
            for link in links:
                link = link.strip() 
                result = get_video_title(link)
                outfile.write(result + '\n')

        print(f"Результаты сохранены в {output_file}")

    except Exception as e:
        print(f"Произошла ошибка при обработке файлов: {e}")

input_file = 'video_links.txt' 
output_file = 'video_titles.txt' 
process_links(input_file, output_file)
