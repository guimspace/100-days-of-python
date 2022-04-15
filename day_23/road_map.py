class RoadMap:
    def __init__(self, num_lanes, block_size, road_length=0):
        self.road_length = road_length
        self.road_width = num_lanes * block_size
        self.block_size = block_size

    def get_center(self, num_lane):
        return (self.block_size - self.road_width) / 2 + num_lane * self.block_size

    def get_middle(self):
        num_blocks = self.road_length / self.block_size
        return 0 if num_blocks % 2 else -self.block_size / 2

    def get_lane(self, num_lane):
        return (1 + num_lane) * self.block_size - self.road_width / 2
