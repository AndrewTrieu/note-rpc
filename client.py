import xmlrpc.client
import requests
from datetime import datetime

# Create a client class


class Client:
    def __init__(self):
        self.server = None

    def connect_server(self):
        try:
            self.server = xmlrpc.client.ServerProxy('http://localhost:7777')
        except ConnectionRefusedError:
            print("Error: Could not connect to server.")
            exit()

    # Start the client
    def start_client(self):
        while True:
            action = input(
                "Options:\n1) Add note\n2) Get notes\n3) Quit\nEnter your choice: ")

            if action == "1":
                # Get user input
                topic = input("Enter the topic: ")
                note = input("Enter the note topic: ")
                text = input("Enter the note text: ")
                date_time = datetime.now()
                timestamp = date_time.strftime("%m/%d/%Y - %H:%M:%S")

                result = self.server.check_topic(topic)
                # Check if the topic exists
                if result:
                    # Append note to existing topic
                    adding = self.server.add_note(topic, note, text, timestamp)
                    if (not adding):
                        print("Error: Could not add note to topic.")
                        return
                else:
                    # Create new topic and add note
                    create = self.server.create_topic(topic)
                    if (not create):
                        print("Error: Could not create topic.")
                        return
                    adding = self.server.add_note(topic, note, text, timestamp)
                    if (not adding):
                        print("Error: Could not add note to topic.")
                        return

                # Ask if user wants to add a link from Wikipedia
                wiki_query = input(
                    "Do you want to add a link to the note topic from Wikipedia? (y/n): ")
                if wiki_query == 'y':
                    search_term = input("Enter search term for Wikipedia: ")
                    wiki_data = requests.get(
                        f"https://en.wikipedia.org/w/api.php?action=opensearch&format=json&search={search_term}").json()
                    if wiki_data[3]:
                        link = wiki_data[3][0]
                    else:
                        no_wiki = print(
                            "No Wikipedia article found!")
                        link = 'No link'
                else:
                    link = "No link"

                # Add the link to the note topic
                add_link = self.server.add_link(topic, link)
                if (not add_link):
                    print("Error: Could not add link to note.")
                    return

            elif action == "2":
                # Get all the notes of a topic
                topic = input("Enter the topic: ")
                notes = self.server.get_notes(topic)
                if (not notes):
                    print("Error: Could not get notes.")
                    return
                print()
                for note in notes:
                    print(
                        f"{note['name']} - {note['text']} ({note['timestamp']}): {note['info']}")
                print()

            elif action == "3":
                # Quit the client
                break

            else:
                print("Invalid option!")


# Run the client
if __name__ == '__main__':
    client = Client()
    client.connect_server()
    client.start_client()
