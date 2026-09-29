namespace EduFlow.Domain.Entities;

public class User
{
    public Guid Id { get; set; }
    public string FullName { get; set; } = string.Empty;
    public string Email { get; set; } = string.Empty;
    public long? TelegramChatId { get; set; }
    public DateTime CreatedAt { get; set; } = DateTime.UtcNow;
}
