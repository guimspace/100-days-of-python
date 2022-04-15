import consts


class RoadMap:
    def get_center(self, num_lane):
        return (consts.BLOCK_SIZE - consts.ROAD_WIDTH) / 2 + num_lane * consts.BLOCK_SIZE

    def get_middle(self):
        num_blocks = consts.ROAD_LENGTH / consts.BLOCK_SIZE
        return 0 if num_blocks % 2 else -consts.BLOCK_SIZE / 2

    def get_lane(self, num_lane):
        return (1 + num_lane) * consts.BLOCK_SIZE - consts.Y_EDGE
