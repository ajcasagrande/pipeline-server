import os
import sys
import subprocess
import pytest

# function to check if the model directory was created properly
def check_directory(path, name, alias, version=1, precision="FP32"):
    # Check to see if folder was created in alias/version path
    model_path = os.path.join(os.path.abspath(path), 'models', alias, str(version))
    assert os.path.isdir(model_path)

    # Check to see if model proc exists
    model_proc_name = name + '.json'
    model_proc_file = os.path.join(model_path, model_proc_name)
    assert os.path.isfile(model_proc_file)

    # Check to see if precision folder exists
    model_precision_path = os.path.join(model_path, precision)
    assert os.path.isdir(model_precision_path)

    # Check to see if xml exists
    model_xml_name = name + '.xml'
    model_xml_file = os.path.join(model_precision_path, model_xml_name)
    assert os.path.isfile(model_xml_file)

    # Check to see if bin exists
    model_bin_name = name + '.bin'
    model_bin_file = os.path.join(model_precision_path, model_bin_name)
    assert os.path.isfile(model_bin_file)
    
# Test the default models from models.list.yml, check to see if in IR and model-proc format
@pytest.mark.skip(reason="skipping until permission issue on openvino-data-dev image is resolved")
def test_mdt_with_default_models_yml(tmpdir,capfd):
    workdir_path = tmpdir.strpath
    model_folder_path = os.path.join(workdir_path, 'models')
    model_download_tool_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../tools/model_downloader')
    model_yml_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../tools/model_downloader/models.list.yml')
    # Run the tool
    results = subprocess.run(['python3', model_download_tool_path, '--model-list', model_yml_path, '--output-dir', workdir_path, '--force'])

    # Set the path of expected output based on the yml file
    model_names = ["mobilenet-ssd", "emotions-recognition-retail-0003", "face-detection-adas-0001", "landmarks-regression-retail-0009", "face-detection-retail-0004", ]
    alias_names = ["object_detection", "emotion_recognition", "face_detection_adas", "landmarks_regression", "face_detection_retail"]
    version = 1

    if results.returncode != 0:
        captured = capfd.readouterr()
        assert 'Necessary tools needed from OpenVINO not found' in captured.out
    else:
        for num, name in enumerate(model_names):
            current_alias = alias_names[num]
            current_version = version
            current_model = name
        
            check_directory(workdir_path, current_model, current_alias, current_version)