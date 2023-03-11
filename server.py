import xmlrpc.server
import xml.etree.ElementTree as ET

# Class to handle the server side of the XML-RPC server


class Server:
    def __init__(self):
        self.db = ET.parse('db.xml')
        self.root = self.db.getroot()

    # Check if the topic exists
    def check_topic(self, topic):
        for child in self.root:
            if child.attrib['name'] == topic:
                return True
        return False

    # Create a new topic if it doesn't exist
    def create_topic(self, topic):
        new_topic = ET.Element('topic', {'name': topic})
        self.root.append(new_topic)
        self.db.write('db.xml')
        return True

    # Add a note of a topic to the database
    def add_note(self, topic, note, text, timestamp):
        for child in self.root:
            if child.attrib['name'] == topic:
                new_note = ET.Element('note', {'name': note})
                new_text = ET.Element('text')
                new_text.text = text
                new_note.append(new_text)
                new_timestamp = ET.Element('timestamp')
                new_timestamp.text = timestamp
                new_note.append(new_timestamp)
                child.append(new_note)
                self.db.write('db.xml')
                return True
        return False

    # Add a Wikipedia link to the note
    def add_link(self, topic, info):
        for child in self.root:
            if child.attrib['name'] == topic:
                # get the last note element
                last_note = child.findall('note')[-1]
                new_info = ET.Element('info')
                new_info.text = info
                last_note.append(new_info)
                self.db.write('db.xml')
                return True
        return False

    # Get all the notes of a topic
    def get_notes(self, topic):
        for child in self.root:
            if child.attrib['name'] == topic:
                notes = []
                for note in child.findall('note'):
                    notes.append({
                        'name': note.attrib['name'],
                        'text': note.find('text').text,
                        'timestamp': note.find('timestamp').text,
                        'info': note.find('info').text
                    })
                return notes


# Start the server
if __name__ == '__main__':
    server = xmlrpc.server.SimpleXMLRPCServer(('localhost', 7777))
    server.register_instance(Server())
    server.serve_forever()
