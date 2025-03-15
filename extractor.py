import os
import cv2
from tqdm import tqdm
import rosbag
import argparse
from cv_bridge import CvBridge
from typing import List


def parse_opt():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description='Example script to demonstrate command line options.')
    # Add options
    parser.add_argument('-s', '--source', type=str, default='Data/ciampino_train_0/ciampino_train0_00.bag', help='Source of files (dir, file, video, ...)')
    parser.add_argument('-o', '--output', type=str, default='Output/', help='Output file path')
    parser.add_argument('-t', '--topics', type=List[str], default=["/camera_left/image_raw", "/camera_right/image_raw"], help='List of topics')
    opt = parser.parse_args()
    return opt


def main(opt):
    # Get information from parsing
    path : str =opt.source
    topics : List[str] =opt.topics
    output_dir : str =opt.output
    bag_name = os.path.basename(path)
    bag_name_without_extension = bag_name[:-4]
    
    # Load the Rosbag
    bag = rosbag.Bag(path)
    # Extract information from bag
    type_and_topic_info = bag.get_type_and_topic_info()

    # Generate dir to save output
    save_path = os.path.join(output_dir, bag_name_without_extension)
    if not os.path.exists(save_path):
        os.makedirs(save_path, exist_ok=True)
    
    for topic in topics:
        print(f"Saving topic {topic}")
        topic_path = os.path.join(save_path, topic.lstrip('/'))
        if not os.path.exists(topic_path):
            print(topic_path)
            os.makedirs(topic_path, exist_ok=True)

        # Get the number of messages for the current topic to set up tqdm
        topic_info = type_and_topic_info.topics[topic]
        num_messages = topic_info.message_count

        # Iterate on the bag
        for i, (topic, msg, t) in tqdm(enumerate(bag.read_messages(topics=[topic])), total=num_messages, desc=f"Processing {topic}", unit="msg"):
            message_type = type(msg).__name__ # Get the message type name as a string

            if message_type == "_sensor_msgs__Image":
                image = CvBridge().imgmsg_to_cv2(msg, "bgr8")
                cv2.imwrite(os.path.join(save_path, topic.lstrip('/')) + "/" + str(i).zfill(6) + ".png", image)

        print(f"Saving topic {topic} completed")

if __name__ == "__main__":
    opt = parse_opt()
    main(opt)