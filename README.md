# Note-Taking Application with XML-RPC

This is a simple note-taking application that allows users to add notes to different topics and retrieve them later. The application uses XML-RPC to communicate between the client and server.

## Getting Started

To use the application, you need to run the `server.py` script first. This starts the XML-RPC server on `localhost:7777`. Once the server is running, you can start the client by running the `client.py` script. The client will prompt you to choose an option:

1. Add note
2. Get notes
3. Quit

## Adding a Note

To add a note, choose option 1 and enter the topic, note name, note text, and optionally a link to a Wikipedia page related to the topic. If the topic already exists, the note will be added to it. Otherwise, a new topic will be created and the note added to it. If a Wikipedia link is added, it will be stored along with the note in the database.

## Getting Notes

To get notes, choose option 2 and enter the topic. The application will retrieve all the notes for the topic and display them on the console. If a Wikipedia link was added to a note, it will be displayed along with the note.

## Quitting

To quit the application, choose option 3.

## Demonstration

This video is recorded for the course CT30A3401 Distributed Systems at LUT University, Finland.

https://user-images.githubusercontent.com/68151686/224495082-f0368d79-c0aa-47ac-9e82-e71f268cc720.mp4

## File Structure

`client.py`: The client script that communicates with the server.

`server.py`: The server script that handles the XML-RPC server and database operations.

`db.xml`: The XML file that stores the notes and topics data.

## Dependencies

`xmlrpc.client`: Required for client-server communication using XML-RPC.

`xmlrpc.server`: Required for server-side XML-RPC implementation.

`requests`: Required for making HTTP requests to retrieve data from Wikipedia API.

`datetime`: Required for generating timestamps for notes.
