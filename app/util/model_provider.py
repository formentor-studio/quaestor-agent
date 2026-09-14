import os
class ModelProvider:

    model_default = "us.amazon.nova-lite-v1:0"

    def get(self) -> str:
        model_orchestrator = os.getenv("AGENT_ORCHESTRATOR", self.model_default)
        if model_orchestrator == "ollama":
          model_orchestrator = self._build_ollama()

        model_journal_entry = os.getenv("AGENT_POST_JOURNAL_ENTRY", self.model_default)
        if model_journal_entry == "ollama":
          model_journal_entry = self._build_ollama()

        return (model_orchestrator, model_journal_entry)

    def _build_ollama(self) -> str:
        from strands.models.ollama import OllamaModel
        return OllamaModel(
          host="http://localhost:11434",
          model_id="qwen3.5:4b-mlx"
        )
