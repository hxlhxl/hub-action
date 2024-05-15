# syntax = docker/dockerfile:1.4.0

FROM golang:1.21.4

RUN go install github.com/cosmtrek/air@latest
# or
# RUN curl -sSfL https://raw.githubusercontent.com/cosmtrek/air/master/install.sh | sh -s -- -b $(go env GOPATH)/bin
