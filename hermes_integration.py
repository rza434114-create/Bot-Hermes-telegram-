"""
Hermes Agent Integration Module
"""

import os
import logging
from typing import Optional
from hermes_agent import HermesAgent, HermesConfig

logger = logging.getLogger(__name__)


class BotHermesIntegration:
    """Integration layer for Hermes Agent with Telegram Bot"""
    
    def __init__(self):
        """Initialize Hermes Agent"""
        self.api_key = os.getenv('HERMES_API_KEY')
        self.model = os.getenv('HERMES_MODEL', 'hermes-2-pro-mistral-7b')
        self.temperature = float(os.getenv('HERMES_TEMPERATURE', 0.7))
        self.max_tokens = int(os.getenv('HERMES_MAX_TOKENS', 1024))
        
        if not self.api_key:
            logger.warning("⚠️ HERMES_API_KEY not set")
            self.agent = None
        else:
            try:
                config = HermesConfig(
                    api_key=self.api_key,
                    model=self.model,
                    temperature=self.temperature,
                    max_tokens=self.max_tokens
                )
                self.agent = HermesAgent(config)
                logger.info("✅ Hermes Agent initialized")
            except Exception as e:
                logger.error(f"❌ Failed to initialize Hermes Agent: {e}")
                self.agent = None
    
    async def generate_response(self, user_message: str) -> str:
        """Generate response using Hermes Agent"""
        if not self.agent:
            return "متاسفانه Hermes Agent فعال نیست. لطفاً تنظیمات را بررسی کنید."
        
        try:
            response = await self.agent.generate(user_message)
            return response
        except Exception as e:
            logger.error(f"❌ Error generating response: {e}")
            return f"خطا در پردازش درخواست: {str(e)}"
