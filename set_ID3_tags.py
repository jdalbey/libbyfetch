import os
import eyed3
# Create an ID3 tag for every mp3 file in the current directory.
# The tag is assigned a title attribute that is the filename (without the extension).
# E.g. the file War_and_Peace.mp3 is assigned a title War_and_Peace

# Function to set the title tag for an mp3 file
def set_title_tag(mp3_file):
    try:
        # Load the mp3 file with eyeD3
        audio_file = eyed3.load(mp3_file)

        # Get the filename without the extension
        title = os.path.splitext(os.path.basename(mp3_file))[0]

        # Check if the file has an existing ID3 tag
        if audio_file.tag is None:
            # If no tag exists, create a new tag
            audio_file.tag = eyed3.id3.tag.Tag()

        # Set the title tag
        audio_file.tag.title = title

        # Save the tag changes
        audio_file.tag.save()

        print(f"ID3 tag updated for: {mp3_file}")

    except Exception as e:
        print(f"Error processing {mp3_file}: {e}")

# Entry point for the application
if __name__ == "__main__":
    # Loop through all files in the current directory
    for filename in os.listdir('.'):
        # Handle only the MP3 files
        if filename.endswith('.mp3'):
            set_title_tag(filename)
