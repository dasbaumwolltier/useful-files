import email
import imaplib

from matrix_client import client, api
from pynodered import node_red, NodeProperty

@node_red(category='pyfuncts')
def get_all_emails_body_unique_and_send_over_matrix_daemons(node, msg):
    connection = imaplib.IMAP4('mail.guldner.eu')

    connection.starttls()
    connection.login('daemons@guldner.eu', 'ebAnbQAANGcAn3GWXHE9vntUqSBmVt2gtwuV2AvcVm6MFrQc5L3CwHua8rJTzyLJQGbjTP5uDZkvB4kHq3EGkqZJ3RRtAXgCUKSt')

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
            msgStr = msg.get_payload()

            if msgStr not in filteredMessages:
                filteredMessages.append(msgStr)

    if len(filteredMessages) == 0:
        return msg

    cli = client.MatrixClient('https://chat.guldner.eu', token='MDAxOGxvY2F0aW9uIGd1bGRuZXIuZXUKMDAxM2lkZW50aWZpZXIga2V5CjAwMTBjaWQgZ2VuID0gMQowMDIzY2lkIHVzZXJfaWQgPSBAbnJlZDpndWxkbmVyLmV1CjAwMTZjaWQgdHlwZSA9IGFjY2VzcwowMDIxY2lkIG5vbmNlID0gRU46LUoxKjdxKmNVfk07SAowMDJmc2lnbmF0dXJlIJ23P_JFtJ1rCFL3jUP6LOnfph0z6_t9uBPsjxmXWxwJCg', user_id='@nred:guldner.eu')
    room: client.Room = cli.join_room('!SmSdHbmEVBqDlcSbug:guldner.eu')

    for message in filteredMessages:
        room.send_text(message)

    for messageNum in messages[0].split(b' '):
        connection.store(messageNum, '+FLAGS', R'\Deleted')