from locust import HttpUser, task, between

class GPTUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def generate_text(self):
        prompt = "Your prompt here"
        self.client.post('/generate-text', json={'prompt': prompt})
