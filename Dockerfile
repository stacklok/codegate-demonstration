FROM alpine:3.14

RUN apk add --no-cache bash openssh-server

COPY ./start_ssh.sh /root/start_ssh.sh

EXPOSE 22

CMD ["/bin/sh", "-c", "/usr/sbin/sshd && /root/start_ssh.sh"]
