using EduFlow.Domain.Entities;

namespace EduFlow.Application.Interfaces;

public interface IUserService
{
    Task<User?> GetByIdAsync(Guid id);
    Task<User> CreateAsync(User user);
}
