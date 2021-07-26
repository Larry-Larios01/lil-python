# procedual paradigma
import os
import csv
current_folder = os.path.dirname(__file__)
CLIENT_TABLE = os.path.join(current_folder, ".clients.csv")

CLIENT_SCHEMA = ['name', 'company', 'email', 'position']
clients = []


def _initialize_clients_from_storage():
    input(CLIENT_TABLE)
    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)

        for row in reader:
            clients.append(row)


def _save_clients_to_storage():
    tmp_table_name = '{}.tmp'.format(CLIENT_TABLE)
    with open(tmp_table_name, mode='w') as f:
        writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)

        os.remove(CLIENT_TABLE)
    os.rename(tmp_table_name, CLIENT_TABLE)


def __name_not_here():
    print('client is not in clients list')


def create_client(client):
    global clients

    if client not in clients:
        clients.append(client)
    else:
        print('CLient already is in the client\'s list')


def list_clients():
    print('uid |  name  | company  | email  | position ')
    print('*' * 50)
    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid=idx,
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position']))


def update_client(client_name, updated_client_name):
    global clients
    if len(clients)-1 >= client_id:
        clients[client_id] = updated_client_name
    else:
        __name_not_here()


def delete_client(client_name):
    global clients

    for idx, client in enumerate(clients):
        if idx == client_id:
            del clients[idx]
            break


def search_client(client_name):

    for client in clients:
        if client != client_name:
            continue
        else:
            return True


def _print_welcome():
    print('welcome to platzi ventas')
    print('*'*50)
    print('what would you do like to do today?')
    print('[C] create client')
    print('[L] list clients')
    print('[U] update client')
    print('[D] delete client')
    print('[S] search client')


def _get_client_field(field_name):
    field = None
    while not field:
        field = input('What is the client {}?'.format(field_name))
        return field


def _get_client_from_user():
    client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position'),
    }
    return client


if __name__ == '__main__':
    _initialize_clients_from_storage()

    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client = _get_client_from_user()
        create_client(client)
        list_clients()
    elif command == 'L':
        list_clients()
    elif command == 'D':
        client_id = int(_get_client_field('id'))
        delete_client(client_id)
    elif command == 'U':
        client_id = int(_get_client_field('id'))
        updated_client = _get_client_from_user()
        update_client(client_id, updated_client)
    elif command == 'S':
        client_name = _get_client_field('name')
        found = search_client(client_name)

        if found:
            print('Client is in the client\'s list')
        else:
            print('The client: {} is not in our client\'s list.'.format(client_name))
    else:
        print('invalid command')
    _save_clients_to_storage()
