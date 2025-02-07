import socket

# 서버 정보
host = "localhost"  # 서버의 IP 주소 (로컬 테스트 시)
port = 12345  # 서버의 포트 번호

# 클라이언트 소켓 생성
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # 서버에 연결
    client_socket.connect((host, port))

    while True:
        # 사용자 입력 받기
        name = "tester77"
        message = input("메시지를 입력하세요 (종료하려면 '끝' 입력): ")

        # 종료 조건
        if message == "끝":
            print("연결 종료 중...")
            break

        # 데이터 전송
        data = f"{name}&&{message}"
        client_socket.send(data.encode("utf-8"))

        # 서버로부터 응답 받기
        try:
            response = client_socket.recv(1024).decode("utf-8")
            print(f"서버 응답: {response}")
        except Exception as e:
            print(f"서버로부터 응답을 받는 중 오류 발생: {e}")
            break

except Exception as e:
    print(f"오류 발생: {e}")

finally:
    # 소켓 닫기
    client_socket.close()
