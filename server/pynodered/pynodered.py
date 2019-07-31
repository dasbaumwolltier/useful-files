import email
import imaplib

from matrix_client import client, api
from pynodered import node_red, NodeProperty

@node_red(category='pyfuncts',
    properties=dict(
        mailserver=NodeProperty('Mailserver'),
        mailbox=NodeProperty('Mailbox'),
        password=NodeProperty('Password'),
        matrixUrl=NodeProperty('Matrix URL'),
        matrixUserId=NodeProperty('Matrix user ID'),
        matrixToken=NodeProperty('Matrix token'),
        matrixRoomId=NodeProperty('Matrix room ID')
    ))
def get_all_emails_body_unique_and_send_over_matrix_daemons(node, msg):
    connection = imaplib.IMAP4(node.mailserver.value)

    connection.starttls()
    connection.login(node.mailbox.value, node.password.value)

    connection.select('INBOX')
    retcode, messages = connection.search(None, '(UNSEEN)')

    filteredMessages = list()

    if retcode == 'OK':
        for messageNum in messages[0].split(b' '):
            print('Fetching message number: ', messageNum)

            if messageNum == b'':
                continue

            _, data = connection.fetch(messageNum, '(RFC822)')
            msg: email.message.Message = email.message_from_bytes(data[0][1])
            msgStr = msg['Subject'] + ':\n\n' + msg.get_payload()

            if msgStr not in filteredMessages:
                filteredMessages.append(msgStr)

    if len(filteredMessages) == 0:
        return msg

    cli = client.MatrixClient(node.matrixUrl.value, token=node.matrixToken.value, user_id=node.matrixUserId.value)
    room: client.Room = cli.join_room(node.matrixRoomId.value)

    for message in filteredMessages:
        room.send_text(message)

    for messageNum in messages[0].split(b' '):
        connection.store(messageNum, '+FLAGS', R'\Deleted')

    retcode, messages = connection.search(None, '(ALL)')
    if(len(messages[0].split(b' ')) >= 1024):
        connection.expunge()
