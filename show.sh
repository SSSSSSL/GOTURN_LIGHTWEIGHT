# DEPLOY_PROTO='./model/tracker.prototxt'
# CAFFE_MODEL='./model/tracker.caffemodel'

# DEPLOY_PROTO='./model/myTracker.prototxt'
# CAFFE_MODEL='./backup/my2Dump_model_iter_55000.caffemodel'

# DEPLOY_PROTO='./model/tiny/tinyTracker_deploy.prototxt'
# CAFFE_MODEL='./backup/tinyDump_model_iter_40000.caffemodel'

# DEPLOY_PROTO='./model/tiny_v2/tiny2Tracker_deploy.prototxt'
# CAFFE_MODEL='./tiny2Dump_model_iter_300000.caffemodel'

DEPLOY_PROTO='./model/tiny_v3/tiny3Tracker_deploy.prototxt'
CAFFE_MODEL='./tiny3Dump_model_iter_66000.caffemodel'

TEST_DATA_PATH='/home/rgblab/tracking/dataset/VOT'

python3 -m show_tracker_vot \
	--p $DEPLOY_PROTO \
	--m $CAFFE_MODEL \
	--i $TEST_DATA_PATH \
	--g 0