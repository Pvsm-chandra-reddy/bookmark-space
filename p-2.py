import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('youtube_videos.db')
cursor = conn.cursor()

# Create a table to store videos if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL,
               link TEXT NOT NULL
    )
''')

# Function to list all videos in the database
def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

# Function to add a new video to the database
def add_video(name, time, link):
    cursor.execute("INSERT INTO videos (name, time, link) VALUES (?, ?, ?)", (name, time, link))
    conn.commit()

# Function to update an existing video in the database
def update_video(video_id, new_name, new_time, new_link):
    cursor.execute("UPDATE videos SET name = ?, time = ?, link = ? WHERE id = ?", (new_name, new_time, new_link, video_id))
    conn.commit()

# Function to delete a video from the database
def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    conn.commit()

# Main function to run the application
def main():
    while True:
        print("\n YouTube Manager App with SQLite")
        print("1. List Videos")
        print("2. Add Video")
        print("3. Update Video")
        print("4. Delete Video")
        print("5. Exit App")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            link = input("Enter the video link: ")
            add_video(name, time, link)
        elif choice == '3':
            video_id = input("Enter video ID to update: ")
            name = input("Enter the new video name: ")
            time = input("Enter the new video time: ")
            link = input("Enter the new video link: ")
            update_video(video_id, name, time, link)
        elif choice == '4':
            video_id = input("Enter video ID to delete: ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid Choice")

    conn.close()

if __name__ == "__main__":
    main()
