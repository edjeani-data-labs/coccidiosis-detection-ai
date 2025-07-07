from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
# from cnnClassifier.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
# from cnnClassifier.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
# from cnnClassifier.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline
# from cnnClassifier.pipeline.stage_06_model_pusher import ModelPusherTrainingPipeline

# STAGE_NAME = "Data Ingestion stage"

# try:
#     logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
#     obj = DataIngestionTrainingPipeline()
#     obj.main()
#     logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
# except Exception as e:
#     logger.exception(e)
#     raise e 


STAGE_NAME = "Prepare base model stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e