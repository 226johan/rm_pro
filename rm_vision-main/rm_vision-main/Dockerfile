FROM ros:humble-ros-base

# setup zsh
RUN sh -c "$(wget -O- https://github.com/deluan/zsh-in-docker/releases/download/v1.1.2/zsh-in-docker.sh)" -- \
    -t jispwoso -p git \
    -p https://github.com/zsh-users/zsh-autosuggestions \
    -p https://github.com/zsh-users/zsh-syntax-highlighting && \
    chsh -s /bin/zsh && \
    rm -rf /var/lib/apt/lists/*

# create workspace
RUN mkdir -p /ros_ws/src
WORKDIR /ros_ws/

# setup scripts
COPY scripts scripts
RUN cat scripts/zshrc >> /root/.zshrc && rm -r scripts
