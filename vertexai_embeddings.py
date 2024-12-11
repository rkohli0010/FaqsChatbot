from vertexai.language_models import TextEmbeddingInput, TextEmbeddingModel
from google.auth import default
from google.cloud import aiplatform
import vertexai

credentials, project = default(quota_project_id='alert-arbor-441919-c4')
aiplatform.init(project=project, credentials=credentials)

def embed_text(text):
  vertexai.init(project = 'alert-arbor-441919-c4')
  dimensionality = 768
  task = "QUESTION_ANSWERING"
  model = TextEmbeddingModel.from_pretrained("text-embedding-005")
  kwargs = dict(output_dimensionality=dimensionality) if dimensionality else {}
  embeddings = model.get_embeddings(text)

  return embeddings



# print(embed_text(["hello there."]))
