const API_BASE = "http://localhost:8000";

// DOM references
const targetBtns = document.querySelectorAll(".target-btn");
const inputText = document.getElementById("inputText");
const convertBtn = document.getElementById("convertBtn");
const resultSection = document.getElementById("resultSection");
const resultText = document.getElementById("resultText");
const copyBtn = document.getElementById("copyBtn");
const errorMsg = document.getElementById("errorMsg");

let selectedTarget = null;

// Target selection
targetBtns.forEach((btn) => {
  btn.addEventListener("click", () => {
    targetBtns.forEach((b) => b.classList.remove("active"));
    btn.classList.add("active");
    selectedTarget = btn.dataset.target;
  });
});

// Convert
convertBtn.addEventListener("click", async () => {
  const text = inputText.value.trim();

  hideError();

  if (!text) {
    showError("변환할 내용을 입력해주세요.");
    return;
  }
  if (!selectedTarget) {
    showError("수신 대상을 선택해주세요.");
    return;
  }

  setLoading(true);
  resultSection.classList.remove("visible");

  try {
    const res = await fetch(`${API_BASE}/api/convert`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text, target_audience: selectedTarget }),
    });

    if (!res.ok) {
      const err = await res.json();
      throw new Error(err.detail || "서버 오류가 발생했습니다.");
    }

    const data = await res.json();
    resultText.textContent = data.converted_text;
    resultSection.classList.add("visible");
  } catch (e) {
    showError(e.message || "변환 중 오류가 발생했습니다. 잠시 후 다시 시도해주세요.");
  } finally {
    setLoading(false);
  }
});

// Copy
copyBtn.addEventListener("click", async () => {
  const text = resultText.textContent;
  if (!text) return;

  try {
    await navigator.clipboard.writeText(text);
    copyBtn.classList.add("copied");
    copyBtn.innerHTML = "✅ 복사됨";
    setTimeout(() => {
      copyBtn.classList.remove("copied");
      copyBtn.innerHTML = "📋 복사하기";
    }, 2000);
  } catch {
    showError("클립보드 복사에 실패했습니다.");
  }
});

function setLoading(on) {
  convertBtn.disabled = on;
  inputText.disabled = on;
  convertBtn.classList.toggle("loading", on);
}

function showError(msg) {
  errorMsg.textContent = msg;
  errorMsg.classList.add("visible");
}

function hideError() {
  errorMsg.classList.remove("visible");
}
