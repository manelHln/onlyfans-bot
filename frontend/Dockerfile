ARG NODE_VERSION=20.11.0

FROM node:${NODE_VERSION}-slim

ENV PNPM_HOME="/pnpm"
ENV PATH="$PNPM_HOME:$PATH"
RUN corepack enable

WORKDIR /usr/src/app/frontend

COPY . .

# RUN npm install -g pnpm

RUN pnpm install

EXPOSE 3000

CMD [ "pnpm", "run", "dev" ]