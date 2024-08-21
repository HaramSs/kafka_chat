from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)


print("채팅 프로그램 - 메시지 발신자")
print("메시지를 입력하세요. (종료 시 'exit' 입력)")

while True:
    msg = input("YOU: ")

    data = {'message': msg, 'time': time.time()}

    if msg.lower() == 'exit':
        producer.close()
        break

    producer.send('chat', value=data)
    producer.flush()


print("채팅이 종료되었습니다.")