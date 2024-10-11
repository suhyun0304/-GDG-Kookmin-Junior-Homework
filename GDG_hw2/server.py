import socket
import pickle

def list_to_dict(dict_values):
    dict_keys = ["이름", "학과", "학번"]
    return dict(zip(dict_keys, dict_values))

if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket 생성
    server_socket.bind(('', 12345)) # socket에 주소 할당
    server_socket.listen(1) # 1명의 클라이언트만 연결 허용

    client1, addr = server_socket.accept() # 클라이언트 연결
    data = client1.recv(1024) # 클라이언트 바이트 데이터 받기
    list_data = list_to_dict(pickle.loads(data)) # 바이트를 리스트로 변환

    print(f"### Recv {list_data}")
    client1.sendall(pickle.dumps(list_data)) # 바이트로 변환해서 클라이언트에 전송

    client1.close() # 클라이언트 소켓 연결 닫기