import socket
import pickle

def create_list():
    return ["이수현", "전자공학부", "20243455"]

if __name__ == '__main__':
    server1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server1.connect(('127.0.0.1', 12345))

    server1.sendall(pickle.dumps(create_list())) # 서버에 데이터 보내기

    data = server1.recv(1024) # 서버에서 바이트 데이터 받기
    dict_list = pickle.loads(data) # 바이트를 리스트로 변환

    print(f"### Send {dict_list}")

    server1.close() # 서버 소켓 연결 닫기