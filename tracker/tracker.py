# Date: Friday 02 June 2017 05:04:00 PM IST 
# Email: nrupatunga@whodat.com
# Name: Nrupatunga
# Description: Basic regressor function implemented

from __future__ import print_function

from helper.image_proc import cropPadImage
from helper.BoundingBox import BoundingBox

import os
import numpy as np


class tracker:
    """tracker class"""

    def __init__(self, objRegressor):
        """TODO: to be defined. """
        _ = objRegressor.regress(np.zeros((50, 50, 3), np.uint8), np.zeros((50, 50, 3), np.uint8))

    def init(self, image_curr, bbox_gt, objRegressor):
        """ initializing the first frame in the video
        """
        self.image_prev = image_curr
        self.bbox_prev_tight = bbox_gt
        self.bbox_curr_prior_tight = bbox_gt

    def update(self, prevFrame, prev_bbox):
        """
        This function allows to update the tracker after another tracking/detection has kicked in.
        :param prevFrame:   last frame before GOTURN algorithm kicks in
        :param prev_bbox:   las position of the tracked object on last frame
        """
        self.image_prev = prevFrame
        self.bbox_curr_prior_tight = prev_bbox
        # self.bbox_prev_tight = prev_bbox

    def track(self, image_curr, objRegressor):
        """TODO: Docstring for tracker.
        :returns: TODO
        """
        target_pad, _, _,  _ = cropPadImage(self.bbox_prev_tight, self.image_prev)
        cur_search_region, search_location, edge_spacing_x, edge_spacing_y = cropPadImage(self.bbox_curr_prior_tight, image_curr)

        bbox_estimate = objRegressor.regress(cur_search_region, target_pad)
        bbox_estimate = BoundingBox(bbox_estimate[0, 0], bbox_estimate[0, 1], bbox_estimate[0, 2], bbox_estimate[0, 3])

        # Inplace correction of bounding box
        bbox_estimate.unscale(cur_search_region)
        bbox_estimate.uncenter(image_curr, search_location, edge_spacing_x, edge_spacing_y)

        self.image_prev = image_curr
        self.bbox_prev_tight = bbox_estimate
        self.bbox_curr_prior_tight = bbox_estimate

        return bbox_estimate