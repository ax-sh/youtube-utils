class YoutubeUtilsLogger:
    def debug(self, msg):
        # For compatibility with youtube-dl, both debug and info are passed into debug
        # You can distinguish them by the prefix '[debug] '
        if msg.startswith('[youtube:tab] '):
            pass
        else:
            self.info(msg)

    def info(self, msg):
        print(msg)
    #     super().info(msg)

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)
