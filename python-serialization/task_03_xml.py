#!/usr/bin/env python3
"""
This module provides functions to serialize a dictionary to an XML file
and deserialize an XML file back into a dictionary using ElementTree.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a dictionary into an XML file.

    Each key-value pair in the dictionary becomes a sub-element
    under the root element <data> in the XML structure.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The name of the file to write the XML data to.
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        element = ET.SubElement(root, key)
        element.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    Deserializes an XML file into a dictionary.

    Parses the XML file assuming a structure where each child of the root
    <data> element represents a key-value pair.

    Args:
        filename (str): The name of the XML file to read from.

    Returns:
        dict: A dictionary reconstructed from the XML data.
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    return {child.tag: child.text for child in root}
